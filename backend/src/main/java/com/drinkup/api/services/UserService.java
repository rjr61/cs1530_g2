package com.drinkup.api.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.drinkup.api.models.User;
import com.drinkup.api.repositories.UserRepository;

@Component
public class UserService {
	
	
	@Autowired
	 private UserRepository userRepo;
	
	public boolean createUser(User user) {
		return userRepo.save(user)!= null;
	} 
	public User getUser(String username) {
		return userRepo.findByUsername(username);
	}
	public boolean checkUser(String username) {
		return userRepo.findByUsername(username)!= null;
	}
	public boolean updateUserList(String username, String postId) {
		User user = userRepo.findByUsername(username);
		if(user!=null) {
			user.addReview(postId);
			createUser(user);
			return true;
		}
		else return false;	
	}
	
}
