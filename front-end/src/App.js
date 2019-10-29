import React, { Component } from 'react';
import { PostBody } from './components/post.js'
import './App.css';
import { Navbar, Nav, Container, Row, Col } from 'react-bootstrap'

// chris stuff
import postData from './data/postdata.json';

class App extends Component {
  constructor(props) {
    super(props)
    this.state={
      users:
      [ 
      ]
    }
    this.handleRefresh = this.handleRefresh.bind(this)
    this.getUser = this.getUser.bind(this)
    this.mapUser = this.mapUser.bind(this)
  }

  handleRefresh() {
    return new Promise((resolve) => {
      this.getNewPosts()
    });
  }


  mapUser(element){
    this.setState({
      users:[
        {
          username: element.username,
          review: element.review,
          location: element.location,
          createdDate: element.createdDate
        },
        ...this.state.users,
      ]
    });
  }

  componentWillMount() {
    this.getUser()
  }

  getUser() {
    fetch('http://localhost:8080/get-posts')
    .then(response => {
      if(response.ok) return response.json();
      throw new Error('Request failed.');
    })
    .then(data => {
      data.forEach(this.mapUser); 
    })
    .catch(error => {
      console.log(error);
    });
  }
  getNewPosts() {
    var time = this.state.users[0].createdDate;
    fetch('http://localhost:8080/get-new',{
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 'time': time }),
    }).then(response => {
      if(response.ok) return response.json();
      throw new Error('Request failed.');
    })
    .then(data => {
      data.forEach(this.mapUser); 
    })
    .catch(error => {
      console.log(error);
    });
  }
  
  render() {
    return (
      <div className="App-content">
        <div className="App-header">
          <Navbar bg="dark" variant="dark" sticky="top">
            <Navbar.Brand href="/">DrinkUp</Navbar.Brand>
            <Nav>
              <Nav.Link href="#feed">Feed</Nav.Link>
            </Nav>
            <Nav>
              <Nav.Link href="#trending">Trending</Nav.Link>
            </Nav>
            <Nav>
              <Nav.Link href="#upload">Upload</Nav.Link>
            </Nav>
          </Navbar>
        </div>
       <div className="App-body">
        {postData.map((user, index) => {
            let username = `${user.username}`
            let location = `${user.location}`
            let review = `${user.review}`
            return(
              <PostBody 
                key={index}
                username={username}
                location={location}
                review={review}
                />
            )
          })}
        </div>
        <div id="refresh-button">Refresh</div>
        {/* 
          {[...this.state.users].map((user, index) => {
            let username = `${user.username}`
            let location = `${user.location}`
            let review = `${user.review}`
            return(
              <PostBody 
                key={index}
                username={username}
                location={location}
                review={review}
                />
            )
          })}
          */}
      </div>
    );
  }
}

export default App;
