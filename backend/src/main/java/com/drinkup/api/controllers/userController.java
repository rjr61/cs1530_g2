package com.drinkup.api.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import com.drinkup.api.models.Post;
import com.drinkup.api.models.User;
import com.drinkup.api.services.UserService;


@CrossOrigin(origins = "http://localhost:3000")
@RestController
public class userController {
	
	@Autowired
	private UserService userService;
	
	 @RequestMapping("/create-user")
	    public ResponseEntity<String> createUser(@RequestBody User user) {
		 	String password = getHashedPassword(user.getPassword());
		 	user =new User(user.getUsername(),password,null);
		 	if(!userService.checkUser(user.getUsername())) {
		    	if(userService.createUser(user)) {
		    		return new ResponseEntity<String>("Successful Post!",HttpStatus.OK);
		    	}
		    	else
		    	{
		    		return new ResponseEntity<String>("Bad post request",HttpStatus.BAD_REQUEST);
		    	}
		 	}else
		 	{
	    		return new ResponseEntity<String>("Bad post request",HttpStatus.BAD_REQUEST);
	    	}
	    }
	 private static String getHashedPassword(String passwordToHash)
	    {
	        try {
	            MessageDigest md = MessageDigest.getInstance("SHA-256");
	            byte[] bytes = md.digest(passwordToHash.getBytes());
	            return new String(bytes);
	        }
	        catch (NoSuchAlgorithmException e)
	        {
	            e.printStackTrace();
	            return null;
	        }
	        
	    }
	 
	 
}
