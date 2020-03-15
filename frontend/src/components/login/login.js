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
        this.handleSubmit.bind(this);
        this.handleChange.bind(this);
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
        console.log(this.state);
    }

    async handleSubmit(event) {
        event.preventDefault();
        const server_response = await fetch("REST", {
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
        return await server_response.json();
    }

    response = (response) => {
        console.log(response.profileObj)
    }

    render() {
        return (
            <Row>
                <Col>
                    <Container className="login-container">
                        <Form className="form" onSubmit={this.handleSubmit}>
                            <Container className="col-11 mt-3">
                                <Form.Group controlId="loginId">
                                    <Form.Label>ID</Form.Label>
                                    <Form.Control size="sm" type="text" placeholder="Enter Email" name="id"></Form.Control>
                                </Form.Group>
                                
                                <Form.Group controlId="loginPassword">
                                    <Form.Label>Password</Form.Label>
                                    <Form.Control size="sm" type="password" placeholder="Enter Password" name="pwd"></Form.Control>
                                </Form.Group>

                                <Button size="sm" variant="primary" type="submit">Log In</Button>
                                <Row><hr className="col-3"/><p className="col-2">OR</p><hr className="col-3"/></Row>
                            </Container>

                            <Container className="mb-2 d-flex justify-content-center google-login">
                                <GoogleLogin
                                    clientId="1078777697294-rs9hoi1i8gr5vvqgeknvs0b67np62j8k.apps.googleusercontent.com"
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