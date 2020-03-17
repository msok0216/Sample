import React from 'react'
import {Row, Col, Nav, Navbar, Form, FormControl, Button} from 'react-bootstrap'


export default class Main extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <>
  <Navbar bg="light" variant="light">
    <Navbar.Brand href="#home">Navbar</Navbar.Brand>
    <Nav className="mr-auto">
      <Nav.Link href="/main">Home</Nav.Link>
      <Nav.Link href="/resource">Resource</Nav.Link>
      <Nav.Link href="/forum">Forum</Nav.Link>
    </Nav>
    <Form inline>
      <FormControl type="text" placeholder="Search" className="mr-sm-2" />
      <Button variant="outline-primary">Search</Button>
    </Form>
  </Navbar>
</>
        )
    }
}