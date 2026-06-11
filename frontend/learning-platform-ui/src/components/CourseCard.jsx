import Card from 'react-bootstrap/Card';
import CardGroup from 'react-bootstrap/CardGroup';

function CourseCard({course}) {
    return (
        <>
            <CardGroup>
                <Card>
                    <Card.Img variant="top" src="holder.js/100px160" />
                    <Card.Body>
                        <Card.Title>{course.title}</Card.Title>
                        <Card.Text>
                            {course.description}
                        </Card.Text>
                    </Card.Body>
                    <Card.Footer>
                        <small className="text-muted">{course.price}</small>
                    </Card.Footer>
                </Card>
            </CardGroup>

        </>
    );
}

export default CourseCard