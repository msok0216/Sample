import React from 'react';
import logo from './logo.svg';
import './App.css';
import LogIn from './components/login/login';
import SignUp from './components/signup/signup';
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
      </Switch>
    </BrowserRouter>
  );
}

export default App;
