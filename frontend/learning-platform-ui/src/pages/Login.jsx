import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/Container';

function Login() {
  return (
    <Container className="d-flex justify-content-center align-items-center vh-100">
      <Card
        className="shadow-lg p-4 border-0"
        style={{ width: '400px', borderRadius: '20px' }}
      >
        <Card.Body>
          <h2 className="text-center mb-4 fw-bold">Welcome Back</h2>

          <Form>
            <Form.Floating className="mb-3">
              <Form.Control
                id="email"
                type="email"
                placeholder="name@example.com"
              />
              <label htmlFor="email">Email Address</label>
            </Form.Floating>

            <Form.Floating className="mb-3">
              <Form.Control
                id="password"
                type="password"
                placeholder="Password"
              />
              <label htmlFor="password">Password</label>
            </Form.Floating>

            <div className="d-flex justify-content-end mb-3">
              <a href="#" className="text-decoration-none">
                Forgot Password?
              </a>
            </div>

            <Button
              variant="primary"
              className="w-100"
              size="lg"
            >
              Login
            </Button>

            <p className="text-center mt-3 text-muted">
              Don't have an account?{" "}
              <a href="/signup" className="text-decoration-none">
                Sign Up
              </a>
            </p>
          </Form>
        </Card.Body>
      </Card>
    </Container>
  );
}

export default Login;