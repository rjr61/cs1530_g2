package com.drinkup.api.services;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;

import com.drinkup.api.services.UserService;
import com.drinkup.api.repositories.PostRepository;
import com.drinkup.api.models.Post;
import org.springframework.stereotype.Component;
@Component
public class PostService {
	
	 @Autowired
	 private PostRepository postRepo;
	 
	 @Autowired
	 private UserService userService;
	 
	 
	 public Post savePost(Post post) {
		 Post savedPost = postRepo.save(post);
		 userService.updateUserList(savedPost.getUsername(), savedPost.getId());
		 return savedPost;
	 }
	 public void deletePosts() {
		 postRepo.deleteAll();
	 }
	 
	 public List<Post> getPosts() {
		List<Post> posts = postRepo.findAll();
		posts = new ArrayList<Post>(posts);
		Collections.sort(posts);
		 return posts;
	 }
	 public Post getPostById(String id) {
		 	Optional<Post> post = postRepo.findById(id);
			return post.get();
		 }
	 public List<Post> getUserPosts(String username) {
			List<Post> posts = postRepo.findAllByUsername(username);
			posts = new ArrayList<Post>(posts);
			Collections.sort(posts);
			 return posts;
		 }
	
	 public List<Post> findByCreatedDateGreaterThan(long cur) {
		 return postRepo.findByCreatedDateGreaterThan(cur);
	 }
}
