import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function Courses() {
  const courses = [
    {
      id: 1,
      title: 'React Fundamentals',
      description: 'Learn components, props, state, and hooks.',
      image: 'https://picsum.photos/300/200?random=1',
    },
    {
      id: 2,
      title: 'Flask Backend',
      description: 'Build REST APIs with Flask and SQLAlchemy.',
      image: 'https://picsum.photos/300/200?random=2',
    },
    {
      id: 3,
      title: 'Database Design',
      description: 'Master SQL, normalization, and relationships.',
      image: 'https://picsum.photos/300/200?random=3',
    },
  ];

  return (
    <Container className="mt-4">
      <h2 className="mb-4">Available Courses</h2>

      <Row>
        {courses.map((course) => (
          <Col md={4} className="mb-4" key={course.id}>
            <Card className="h-100 shadow-sm">
              <Card.Img
                variant="top"
                src={course.image}
                style={{ height: '200px', objectFit: 'cover' }}
              />

              <Card.Body className="d-flex flex-column">
                <Card.Title>{course.title}</Card.Title>

                <Card.Text>
                  {course.description}
                </Card.Text>

                <Button
                  variant="primary"
                  className="mt-auto"
                >
                  View Course
                </Button>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
    </Container>
  );
}

export default Courses;