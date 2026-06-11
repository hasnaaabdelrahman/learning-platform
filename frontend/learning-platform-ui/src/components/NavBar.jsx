import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import { LinkContainer } from 'react-router-bootstrap';

function NavBar() {
  return (
    <Navbar
      expand="lg"
      bg="dark"
      variant="dark"
      sticky="top"
      className="shadow-sm"
    >
      <Container>
        <LinkContainer to="/">
          <Navbar.Brand className="fw-bold">
            📚 Learning Platform
          </Navbar.Brand>
        </LinkContainer>

        <Navbar.Toggle aria-controls="navbarScroll" />

        <Navbar.Collapse id="navbarScroll">
          <Nav className="me-auto">
            <LinkContainer to="/">
              <Nav.Link>Home</Nav.Link>
            </LinkContainer>

            <LinkContainer to="/courses">
              <Nav.Link>Courses</Nav.Link>
            </LinkContainer>

            <NavDropdown title="Account" id="navbarScrollingDropdown">
              <LinkContainer to="/login">
                <NavDropdown.Item>Login</NavDropdown.Item>
              </LinkContainer>

              <LinkContainer to="/signup">
                <NavDropdown.Item>Sign Up</NavDropdown.Item>
              </LinkContainer>

              <NavDropdown.Divider />

              <LinkContainer to="/my-courses">
                <NavDropdown.Item>My Courses</NavDropdown.Item>
              </LinkContainer>
            </NavDropdown>
          </Nav>

          <Form className="d-flex">
            <Form.Control
              type="search"
              placeholder="Search courses..."
              className="me-2"
            />
            <Button variant="outline-light">
              Search
            </Button>
          </Form>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavBar;