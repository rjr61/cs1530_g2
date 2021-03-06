package com.drinkup.api.repositories;

import com.drinkup.api.models.Post;

import java.util.List;
import java.util.Optional;

import org.socialsignin.spring.data.dynamodb.repository.EnableScan;
import org.springframework.data.repository.CrudRepository;

@EnableScan
public interface PostRepository extends CrudRepository<Post, String> {

	Optional<Post> findById(String id);
	
	List<Post> findAll();
	List<Post> findAllByUsername(String username);
	
	List<Post> findAllOrderByCreatedDate();
	
	List<Post> findByCreatedDateGreaterThan(long cur);
	
	@SuppressWarnings("unchecked")
	Post save(Post item);
	
	void deleteAll();
}