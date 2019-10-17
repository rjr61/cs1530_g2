package com.drinkup.api.repositories;

import com.drinkup.api.models.Post;
import com.drinkup.api.models.User;
import java.util.List;
import java.util.Optional;
import org.socialsignin.spring.data.dynamodb.repository.EnableScan;
import org.springframework.data.repository.CrudRepository;

@EnableScan
public interface UserRepository  extends CrudRepository<User, String>{
	@SuppressWarnings("unchecked")
	User save(User user);
	User findByUsername(String username);
		
}
