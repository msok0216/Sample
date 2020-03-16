import React from 'react'
import {Row, Col, Form, Container, Button} from 'react-bootstrap';

export default class SignUp extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            name: "",
            id: "",
            pwd: "",
            pwd2: "",
            email: "",
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.response = this.response.bind(this);
    }

    response = (response) => {
        console.log(response.profileObj)
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
        console.log(this.state);
    };

    async handleSubmit(event) {
        console.log(JSON.stringify(this.state));
        event.preventDefault();
        const server_response = await fetch("/signup", {
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
        return await server_response.json();
    }

    render() {
        return (
            <Row>
                <Col>
                    <Container className="signup-container">
                        <Form className="form" onSubmit={this.handleSubmit}>
                            <Container className="col-11 mt-3">
                                <Form.Group controlId="signupName">
                                    <Form.Label>Name</Form.Label>
                                    <Form.Control size="sm" type="name" placeholder="Enter Name" name="name" onChange={this.handleChange}></Form.Control>
                                </Form.Group>
                                
                                <Form.Group controlId="signupId">
                                    <Form.Label>ID</Form.Label>
                                    <Form.Control size="sm" type="Id" placeholder="Enter User ID" name="id" onChange={this.handleChange}></Form.Control>
                                </Form.Group>

                                <Form.Group controlId="signupPassword">
                                    <Form.Label>Password</Form.Label>
                                    <Form.Control size="sm" type="password" placeholder="Enter Password" name="pwd" onChange={this.handleChange}></Form.Control>
                                </Form.Group>

                                <Form.Group controlId="signupConfirmPassword">
                                    <Form.Label>Confirm Password</Form.Label>
                                    <Form.Control size="sm" type="confirmPassword" placeholder="Enter Password" name="pwd2" onChange={this.handleChange}></Form.Control>
                                </Form.Group>

                                <Form.Group controlId="signupEmail">
                                    <Form.Label>Email</Form.Label>
                                    <Form.Control size="sm" type="email" placeholder="Enter Email" name="email" onChange={this.handleChange}></Form.Control>
                                </Form.Group>

                                <Button size="sm" variant="primary" type="submit" className="mt-2 mb-2">Sign Up</Button>
                            </Container>

                        </Form>
                    </Container>

                </Col>
            </Row>
        )
    }
}