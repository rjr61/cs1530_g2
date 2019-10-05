package com.drinkup.api.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;


import com.drinkup.api.repositories.PostRepository;
import com.drinkup.api.models.Post;
import org.springframework.stereotype.Component;
@Component
public class PostService {
	
	 @Autowired
	 private PostRepository postRepo;
	 
	 public Post savePost(Post post) {
		 return postRepo.save(post);
	 }
	 public List<Post> getPosts() {
		 return postRepo.findAll();
	 }
	 

}
