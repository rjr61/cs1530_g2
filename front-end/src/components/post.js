import React from 'react';
import './post.css'

const PostBox = (props) => {
  return(
    <div className="post-body">
      {props.children}
    </div>
  )
}

/*
const Location = (props) => {
  return(
    <div className="location">
      {props.location}
    </div>
  )
}
*/

const Username = (props) => {
  return(
    <div className="post-username">
      {props.username}
    </div>
  )
}

const Review = (props) => {
  return(
    <div className="post-review">
      {props.review}
    </div>
  )
}

const PostBody = (props) => {
  return(
    <PostBox>
        <Username username={props.username}/>
        <Review review={props.review}/>
        {/*<Location location={props.location}/>*/}
    </PostBox>
  )
}

export { PostBody }