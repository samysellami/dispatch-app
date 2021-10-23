import React, { useEffect, useState } from 'react'
import { Form, Button, Container, Row, Col } from 'react-bootstrap'

import axios from 'axios'
import Message from './Message'
import Loader from './Loader'

function HomeScreen() {
    const [name, setName] = useState('')
    const [email, setEmail] = useState('')
    const [phone, setPhone] = useState('')
    const [subject, setSubject] = useState('')
    const [message, setMessage] = useState('')
    const [response, setResponse] = useState('')
    const [error, setError] = useState('')
    const [loading, setLoading] = useState(false)

    const submitHandler = (e) => {
        e.preventDefault()
        setError('')
        setResponse('')

        const notif = {
            name: name,
            subject: subject,
            email: email,
            phoneNumber: phone,
            message: message,
        }
        sendData(notif)
    }

    const sendData = async (notif) => {
        try {
            setLoading(true)
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                },
            }
            const { data } = await axios.post(`/api/`, notif, config)

            setResponse(data['detail'])
        } catch (errors) {
            setError(
                errors.response && errors.response.data.detail
                    ? errors.response.data.detail
                    : errors.message
            )
        } finally {
            setLoading(false)
        }
    }

    useEffect(() => {
        setName('')
        setEmail('')
        setMessage('')
        setPhone('')
        setSubject('')
    }, [response, error])

    return (
        <Container>
            <Row className='justify-content-md-center my-5'>
                <Col xs={12} md={6} lg={6}>
                    <h1>Send notification</h1>

                    {loading && <Loader />}
                    {response && <Message variant='info'>{response}</Message>}
                    {error && <Message variant='danger'>{error}</Message>}

                    <Form onSubmit={submitHandler} id='send-notif-form'>
                        <Form.Group className='mb-3' controlId='name'>
                            <Form.Label>Full Name</Form.Label>
                            <Form.Control
                                type='name'
                                placeholder='John Doe'
                                value={name}
                                onChange={(e) => setName(e.target.value)}
                            ></Form.Control>
                        </Form.Group>

                        <Form.Group className='mb-3' controlId='email'>
                            <Form.Label>Email Address</Form.Label>
                            <Form.Control
                                required
                                type='email'
                                placeholder='name@example.com'
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                            ></Form.Control>
                        </Form.Group>

                        <Form.Group controlId='phone'>
                            <Form.Label>Phone Number</Form.Label>
                            <Form.Control
                                type='textarea'
                                placeholder='+7 xxx xxx xx xx'
                                value={phone}
                                onChange={(e) => setPhone(e.target.value)}
                            ></Form.Control>
                        </Form.Group>

                        <Form.Group className='mb-3' controlId='subject'>
                            <Form.Label>Subject</Form.Label>
                            <Form.Control
                                type='textarea'
                                placeholder='subject'
                                value={subject}
                                as='textarea'
                                rows={1}
                                onChange={(e) => setSubject(e.target.value)}
                            ></Form.Control>
                        </Form.Group>

                        <Form.Group className='mb-3' controlId='message'>
                            <Form.Label>Message</Form.Label>
                            <Form.Control
                                required
                                type='textarea'
                                placeholder='Your message'
                                value={message}
                                as='textarea'
                                rows={5}
                                onChange={(e) => setMessage(e.target.value)}
                            ></Form.Control>
                        </Form.Group>

                        <Button type='submit' variant='primary' disabled={loading}>
                            Send
                        </Button>
                    </Form>
                </Col>
            </Row>
        </Container>
    )
}

export default HomeScreen
