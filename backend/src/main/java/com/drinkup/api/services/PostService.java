package com.drinkup.api.services;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;

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
		List<Post> posts = postRepo.findAll();
		posts = new ArrayList<Post>(posts);
		Collections.sort(posts);
		//Collections.reverse(posts);
		 return posts;
	 }
	
	 public List<Post> findByCreatedDateGreaterThan(long cur) {
		 return postRepo.findByCreatedDateGreaterThan(cur);
	 }
	 
	 

}
