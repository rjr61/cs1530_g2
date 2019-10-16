package com.drinkup.api;
import java.util.Collections;
import java.util.Date;
import java.text.DateFormat;
import java.text.ParseException;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.drinkup.api.models.*;
import com.drinkup.api.services.PostService;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.http.ResponseEntity.BodyBuilder;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.CrossOrigin;
@CrossOrigin(origins = "http://localhost:3000")
@RestController
public class postController {
	
	@Autowired
	private PostService postService;
	
	
    @RequestMapping("/save-post")
    public ResponseEntity<String> savePost(@RequestBody Post post) {
    	Post savedPost = postService.savePost(post);
    	if(savedPost!=null) {
    		return new ResponseEntity<String>("Successful Post!",HttpStatus.OK);
    	}else
    	{
    		return new ResponseEntity<String>("Bad post request",HttpStatus.BAD_REQUEST);
    	}
    }
    @RequestMapping("/get-posts")
    public List<Post> getPosts() {
    	List<Post> posts = postService.getPosts();
    	posts = (List<Post>)posts;
    	if(posts!=null) {
    		Collections.sort(posts);
    		Collections.reverse(posts);
    		return posts;
    	}else
    	{
    		return null;
    	}
    }
    @RequestMapping("/get-new")
    public List<Post> getCurrentPosts(@RequestBody Time cur) throws ParseException {
		List<Post> posts = postService.findByCreatedDateGreaterThan(cur.getTime());
    	if(posts!=null) {
    		return posts;
    	}else
    	{
    		return null;
    	}
    }

}