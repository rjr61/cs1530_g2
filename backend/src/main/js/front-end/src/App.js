import React, { Component } from 'react';
import { PostBody } from './components/tweet.js'
import {PullToRefresh, PullDownContent, ReleaseContent, RefreshContent} from "react-js-pull-to-refresh";
import './App.css';

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
      this.getUser()
    });
  }


  mapUser(element){
    this.setState({
      users:[
        {
          username: element.username,
          review: element.review,
          location: element.location,
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
  
  render() {
    return (
      <PullToRefresh
      pullDownContent={<PullDownContent />}
      releaseContent={<ReleaseContent />}
      refreshContent={<RefreshContent />}
      pullDownThreshold={2}
      onRefresh={this.handleRefresh}
      triggerHeight={50}
      backgroundColor='black'>
      <div className="main-body">
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
      </PullToRefresh>
    );
  }
}

export default App;
