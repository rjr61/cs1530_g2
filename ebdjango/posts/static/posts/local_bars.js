var substringMatcher = function(strs) {
    return function findMatches(q, cb) {
      var matches, substrRegex;
  
      // an array that will be populated with substring matches
      matches = [];
  
      // regex used to determine if a string contains the substring `q`
      substrRegex = new RegExp(q, 'i');
  
      // iterate through the pool of strings and for any string that
      // contains the substring `q`, add it to the `matches` array
      $.each(strs, function(i, str) {
        if (substrRegex.test(str)) {
          matches.push(str);
        }
      });
  
      cb(matches);
    };
  };
  
  var bars = ['1311', '1947 Tavern', '20th Street Bar & Grill (New Feb 2015)', '5801 Video Lounge & Cafe', 'Acacia', 'Alexander’s', 'Antoon’s Pizza', 'Apple Inn', 'Archie’s Bar', 'Arsenal Cider House', 'Arsenal Lanes', 'August Henry’s City Saloon', 'AVA Lounge', 'Bangkok Balcony', 'Bar 11', 'Beehive Coffeehouse', 'Belvedere’s', 'Bigham Tavern', 'Birmingham Bridge Tavern', 'Bites and Brews', 'Bloomfield Bridge Tavern', 'Blue Moon', 'Bootleggers', 'Brewski’s', 'BRGR', 'Brillobox', 'Buckhead Saloon', 'Buffalo Blues', 'Butterjoint', 'Cafe’ Niko’s', 'Caliente Pizza and Bar', 'Cappy’s Cafe', 'Capri Pizzeria', 'Carmella’s Plates & Pints', 'Carson Street Deli & Craft Beer Bar', 'Casbah', 'Cattivo', 'Cheesecake Factory', 'Church Brew Works', 'Corner Cafe', 'Cupka’s Cafe 2', 'D’s Six Pax & Dogz', 'Dee’s Cafe', 'Del’s Bar & Restaurant', 'Devils and Dolls', 'Double Wide Grill', 'Dunning’s Grill', 'Easy Street', 'Eclipse Lounge', 'Eleven Contemporary Kitchen', 'Emilianos Mexican Restaurant', 'Excuses Bar and Grill', 'Fuel & Fuddle', 'Garage Door Saloon', 'Gene’s Place', 'Gorman’s Pub', 'Graziano’s Pizzeria', 'Hambone’s Pub', 'Hard Rock Cafe', 'Harris Grill', 'Hemingway’s Cafe', 'Hofbräuhaus Pittsburgh', 'Hot Rod Cafe', 'Hough’s Taproom & BrewPub', 'Howlers Coyote Cafe', 'Images Bar', 'Industry Public House', 'Jack’s Bar', 'Jekyl & Hyde', 'Jimmy D’s', 'Joe & Pie', 'Kelly’s Bar and Lounge', 'Lava Lounge', 'Le Mardi Gras', 'local bar + kitchen', 'Logan’s Pub', 'Lombardozzi’s Restaurant', 'Lot 17 Bar & Grill', 'Lou’s Little Corner Bar', 'Mad Mex', 'Mad Mex', 'Mario’s East Side Saloon', 'Mario’s South Side Saloon', 'Micro Diner', 'Milkshake Factory', 'Mineo’s Pizza House', 'Mint Hookah Bar & Lounge', 'Mitchell’s Tavern', 'Murphy’s Tap Room', 'Murray Avenue Grill', 'Nadine’s Bar & Restaurant', 'Nakama', 'Napoli’s Pizzeria', 'New Amsterdam', 'New Dumpling House', 'Nico’s Recovery Room', 'Nied’s Hotel', 'Nola on the Square', 'Olio Trattoria', 'Over The Bar Bicycle Cafe', 'Packs & Dogs', 'Papa DaVinci', 'Peter’s Pub', 'Piper’s Pub', 'Pizza Bellino', 'Pizza Parma', 'Pizza Romano', 'Pizza Sola', 'Pleasure Bar & Restaurant', 'Poppy’s Bistro & Pub', 'Potatoheads Bar and Grill', 'Pregame Bar', 'Primanti Bros.', 'Primanti Bros. South Side', 'Prince of India', 'Pusadee’s Garden', 'Quaker Steak & Lube', 'Redbeard’s Bar & Grill', 'Remedy', 'Round Corner Cantina', 'Ruggers Pub', 'Rusty Barrel Saloon', 'Ryan’s Pub & Grill', 'S. Aiken Bar and Grille', 'Sakura Teppanyaki & Sushi', 'Salt of the Earth', 'Satalio’s', 'Scarpaci’s', 'Shady Grove', 'Shadyside Hideaway Bar', 'Shiloh Grill', 'Silky’s Olde Thyme Pub', 'Sloppy Joe’s', 'Smokin’ Joe’s Saloon', 'SOBA Lounge', 'Social at Bakery Square', 'Sonny’s Tavern', 'Sonoma Grille', 'Sorrento’s Pizza Roma', 'South Side BBQ Company', 'Sphinx Cafe', 'Spin Bartini & Ultra Lounge', 'Spoon', 'Squirrel Hill Cafe', 'Stack’d Burgers & Beer', 'Steel Cactus', 'Stinky’s Bar and Grill', 'Streets on Carson', 'Sushi Too', 'Take A Break', 'Taste Of India', 'Tavern 245', 'Tender Bar + Kitchen', 'Tessaro’s', 'Thai Place', 'The Allegheny Wine Mixer', 'The Library', 'The Map Room', 'The Original Hot Dog Shop', 'The Rowdy Buck', 'The Smiling Moose', 'The South Paw', 'The Summit', 'The Urban Tap', 'The Yard', 'Thunderbird Cafe', 'Tiki Lounge', 'Toro’s Tavern', 'Trapuzzano Italian Chophouse', 'Twelve on Carson', 'Uncle Jimmy’s Tavern', 'Union Grill', 'Vocelli Pizza', 'William Penn Tavern', 'XO Cafe & Lounge'];
  
  $('#the-basics .typeahead').typeahead({
    hint: true,
    highlight: true,
    minLength: 1
  },
  {
    name: 'bars',
    source: substringMatcher(bars)
  });