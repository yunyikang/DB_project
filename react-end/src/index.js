import React from 'react';
import ReactDOM from 'react-dom';
import { Route, BrowserRouter as Router } from 'react-router-dom'
import Home from './Home';
import AddBook from './AddBook';
import Browse from './Browse';
import Book from './Book';
import Log from './Log';
import SignUp from './Signup';
import SignIn from './SignIn';
import SearchResults from './SearchResults';

const routing = (
    <Router>
        <div>
            <Route exact path="/" component={Home} />
            <Route path="/signin" component={SignIn} />
            <Route path="/signup" component={SignUp} />
            <Route path="/browse" component={Browse} />
            <Route path="/searchresults/:searchstring" component={SearchResults} />
            <Route path='/books/:bookid' component={Book} />
            <Route path='/addbook' component={AddBook} />
            <Route path='/log' component={Log} />
        </div>
    </Router>
)

ReactDOM.render(routing, document.getElementById('root'));

