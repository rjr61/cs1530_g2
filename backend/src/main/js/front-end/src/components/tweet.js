import React from 'react';

const PostBox = (props) => {
  return(
    <div className="post-body">
      {props.children}
    </div>
  )
}

/*const Image = (props) => {
  return(
    <img src={props.image} alt="Logo" className="picture">
    </img>
  )
}*/

const Location = (props) => {
  return(
    <div className="location">
      {props.location}
    </div>
  )
}

const Username = (props) => {
  return(
    <div className="username">
      {props.username}
    </div>
  )
}

const Review = (props) => {
  return(
    <div className="review">
      {props.review}
    </div>
  )
}

const PostBody = (props) => {
  return(
    <PostBox>
      <div className="inner-body">
        <div className="body">
          <div className="inner-body">
            <Username username={props.username}/>
            <Location location={props.location}/>
          </div>
          <Review review={props.review}/>
        </div>
      </div>
    </PostBox>
  )
}

export { PostBody }