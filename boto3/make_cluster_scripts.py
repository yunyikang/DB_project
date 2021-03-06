import os

import fire


def main(num_nodes, instance_type="t2.micro", ami="ami-00068cd7555f543d5"):
    # Amazon Linux 2 AMI (HVM), SSD Volume Type
    # Same hdfs/spark version as Amazon EMR
    # Use default EMR_EC2 IAM Role to access S3 bucket

    with open("info.txt") as f:
        dict_info = eval(f.read())
    keyfile = dict_info["keyfile"]
    keyname = dict_info["keyname"]
    region = dict_info["region"]

    def write_script(lines, path):
        print("Writing script to:", path)
        with open(path, "w") as f:
            f.write("\n".join(lines))

    # Use role="EMR_EC2_DefaultRole" so we don't have to set up ourselves
    lines = [
        "#!/bin/bash",
        "flintrock launch my-cluster \\",
        "--install-hdfs \\",
        "--hdfs-version 2.8.5 \\",
        "--install-spark \\",
        "--spark-version 2.4.4 \\",
        "--ec2-user ec2-user \\",
        "--ec2-instance-profile-name EMR_EC2_DefaultRole \\",
        "--ec2-key-name {} \\".format(keyname),
        "--ec2-region {} \\".format(region),
        "--ec2-identity-file {} \\".format(keyfile),
        "--ec2-instance-type {} \\".format(instance_type),
        "--ec2-ami {} \\".format(ami),
        "--num-slaves {} \\".format(num_nodes - 1),
    ]
    write_script(lines, "cluster_launch.sh")

    lines = [
        "#!/bin/bash",
        "flintrock login my-cluster \\",
        "--ec2-user ec2-user \\",
        "--ec2-identity-file {} \\".format(keyfile),
    ]
    write_script(lines, "cluster_login.sh")

    lines = ["#!/bin/bash", "flintrock destroy my-cluster --assume-yes"]
    write_script(lines, "cluster_terminate.sh")

    lines = [
        "#!/bin/bash",
        "flintrock copy-file --assume-yes my-cluster $1 /home/ec2-user/$1 \\",
        "--ec2-user ec2-user \\",
        "--ec2-identity-file {} \\".format(keyfile),
    ]
    write_script(lines, "cluster_copy_file.sh")

    lines = [
        "#!/bin/bash",
        "curl -O https://bootstrap.pypa.io/get-pip.py",
        "bash cluster_copy_file.sh get-pip.py",
        "bash cluster_run_command.sh 'sudo python get-pip.py && sudo pip install numpy'",
    ]
    write_script(lines, "cluster_install_numpy.sh")

    lines = [
        "#!/bin/bash",
        "flintrock run-command my-cluster \\",
        "--ec2-user ec2-user \\",
        "--ec2-identity-file {} \\".format(keyfile),
        "-- $1",  # "--" prevents flintrock from parsing anymore flags
    ]
    write_script(lines, "cluster_run_command.sh")

    # spark_submit prefix with --packages argument to enable access to S3
    spark_submit = "spark-submit --packages org.apache.hadoop:hadoop-aws:2.7.6"
    lines = [
        "#!/bin/bash",
        "bash cluster_copy_file.sh $1",
        "flintrock run-command my-cluster '{}' $1 \\".format(spark_submit),
        "--ec2-user ec2-user \\",
        "--ec2-identity-file {} \\".format(keyfile),
        "--master-only \\",
    ]
    write_script(lines, "cluster_run_app.sh")


if __name__ == "__main__":
    fire.Fire(main)
