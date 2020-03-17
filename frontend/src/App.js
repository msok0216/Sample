import React from 'react';
import logo from './logo.svg';
import './App.css';
import LogIn from './components/login/login';
import SignUp from './components/signup/signup';
import Main from './components/main/main';
import Stat from './components/main/stat/stat';
import { BrowserRouter, Switch, Route, Link } from 'react-router-dom';


function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/login">
          <LogIn/>
        </Route>

        <Route path="/signup">
          <SignUp/>
        </Route>

        <Route path="/main">
          <Main/>
        </Route>

        <Route path="/main/stats">
          <Stat/>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
