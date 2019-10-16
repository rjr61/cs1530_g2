import React, { Component } from 'react';
import { PostBody } from './components/post.js'
import './App.css';
import Navbar from 'react-bootstrap/Navbar'

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
        <Navbar>
          <Navbar.Brand href="#home">Navbar with text</Navbar.Brand>
          <Navbar.Toggle />
          <Navbar.Collapse className="justify-content-end">
            <Navbar.Text>
              Signed in as: <a href="#login">Mark Otto</a>
            </Navbar.Text>
          </Navbar.Collapse>
        </Navbar>
        </div>
        <div className="App-body">
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
        </div>
      </div>
    );
  }
}

export default App;
