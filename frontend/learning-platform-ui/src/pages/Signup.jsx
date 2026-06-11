import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/Container';

function Signup() {
  return (
    <Container
      className="d-flex justify-content-center align-items-center vh-100"
    >
      <Card
        className="shadow-lg p-4 border-0"
        style={{ width: '450px', borderRadius: '20px' }}
      >
        <Card.Body>
          <h2 className="text-center mb-4 fw-bold">Create Account</h2>

          <Form>
            <Form.Floating className="mb-3">
              <Form.Control
                id="firstName"
                type="text"
                placeholder="John"
              />
              <label htmlFor="firstName">First Name</label>
            </Form.Floating>

            <Form.Floating className="mb-3">
              <Form.Control
                id="lastName"
                type="text"
                placeholder="Doe"
              />
              <label htmlFor="lastName">Last Name</label>
            </Form.Floating>

            <Form.Floating className="mb-3">
              <Form.Control
                id="email"
                type="email"
                placeholder="name@example.com"
              />
              <label htmlFor="email">Email Address</label>
            </Form.Floating>

            <Form.Floating className="mb-4">
              <Form.Control
                id="password"
                type="password"
                placeholder="Password"
              />
              <label htmlFor="password">Password</label>
            </Form.Floating>

            <Button
              variant="primary"
              size="lg"
              className="w-100"
            >
              Sign Up
            </Button>

            <p className="text-center mt-3 text-muted">
              Already have an account?{" "}
              <a href="/login" className="text-decoration-none">
                Login
              </a>
            </p>
          </Form>
        </Card.Body>
      </Card>
    </Container>
  );
}

export default Signup;