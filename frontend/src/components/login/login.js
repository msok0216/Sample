import React from 'react'
import {Row, Col, Form, Container, Button} from 'react-bootstrap';
import { GoogleLogin } from 'react-google-login';
import { Link } from 'react-router-dom';

import './login.css';

export default class LogIn extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            isSignedIn: false,
            id:"",
            pwd:""
        }
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.google_api_key = `${process.env.GOOGLE_LOGIN_KEY}.apps.googleusercontent.com`
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
        console.log(this.state);
    }

    async handleSubmit(event) {
        event.preventDefault();
        const server_response = await fetch("/login", {
            method: 'POST',
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }, 
            redirect: 'follow',
            body: JSON.stringify(this.state)
        })
        .then(response => {
            localStorage.setItem('token', response.json['token'])
            // TODO add redirect
        })
        .catch(err => {
            console.log(err)
        })

    }

    // response = (response) => {
    //     console.log(response.profileObj)
    // }

    render() {
        return (
            <Row>
                <Col>
                    <Container className="login-container">
                        <Form className="form" onSubmit={this.handleSubmit}>
                            <Container className="col-11 mt-3">
                                <Form.Group controlId="loginId">
                                    <Form.Label>ID</Form.Label>
                                    <Form.Control size="sm" type="text" placeholder="Enter Email" name="id" onChange={this.handleChange}></Form.Control>
                                </Form.Group>
                                
                                <Form.Group controlId="loginPassword">
                                    <Form.Label>Password</Form.Label>
                                    <Form.Control size="sm" type="password" placeholder="Enter Password" name="pwd" onChange={this.handleChange}></Form.Control>
                                </Form.Group>

                                <Button size="sm" variant="primary" type="submit">Log In</Button>
                                <Row><hr className="col-3"/><p className="col-2">OR</p><hr className="col-3"/></Row>
                            </Container>

                            <Container className="mb-2 d-flex justify-content-center google-login">
                                <GoogleLogin
                                    clientId= {this.google_api_key}
                                    buttonText="Login"
                                    onSuccess={this.response}
                                    onFailure={this.response}
                                    cookiePolicy={'single_host_origin'}
                                    isSignedIn={true}
                                />
                            </Container>
                        </Form>
                    </Container>

                    <Container className="login-container mt-1">
                        <Form className="form text-center">
                            <p className="mt-1">
                                Don't have an account?<br/>
                                <Link to="/signup">Create an account</Link>
                            </p>
                        </Form>
                    </Container>
                </Col>
            </Row>
        )
    }
}