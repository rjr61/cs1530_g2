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
  
  var states = ['TTMS INC', "HEMINGWAY'S CAFE", 'ORIGINAL HOT DOG SHOP', 
  'MAGEE-WOMENS HOSPITAL', 'MELLINGER BEER DISTRIBUTOR, INC.  ', 
  'GATEWAY WINE & SPIRITS, INC.', 'MAD MEX', 'ANDREA CORTESE-HASSETT,PHD ITX M DIAGNOSTICS', 
  'UNION GRILL', 'THE TWENTIETH CENTURY CLUB', 'PRINCE OF INDIA RESTAURANT & TAVERN, INC.', 
  'AMERICANA BAR CORPORATION', 'PIV-CON, INC.', "HIEBER'S PHARMACY, INC.", 
  'SCHENLEY CENTER ASSOCIATES, L.P. & CROSSROADS HOSPITALITY CO., L.L.C.', 
  'CARNEGIE MUSEUM OF NATURAL HISTORY', 'KOREA GARDEN', "GENE'S PLACE", 
  'PHIPPS CONSERVATORY AND BOTANICAL GARDENS INC', 'THE SPICE ISLAND TEA HOUSE', 
  'SOUTH SIDE SIN CITY INC', 'P TOWN', 'CRAIG DISTRIBUTING COMPANY', 
  'UNIVERSITY OF PITTSBURGH OF THE COMMONWEALTH SYSTEM OF HIGHER ED', 
  'SOLDIERS & SAILORS MEMORIAL HALL & MUSEUM TRUST INC', 'LEGUME INC', 
  'BLACK BEAN CUBAN CUISINE', "PITT'S DOGG'N IT LLC", 
  'URGO HOTELS LP AND RLJ III - HGN PITTSBURGH LESSEE LP', 
  "EAT'N PARK HOSPITALITY GROUP INC", 'ALI-BABA', 'WYNDHAM PITTSBURGH UNIVERSITY CENTER', 
  'CAMPUS BOOKSTORE INC', 'CREPES PARISIENNES LLC', 'KBOX KARAOKE HOUSE', 
  'UPMC PRESBYTERIAN SHADYSIDE PRESBYTERIAN CAMPUS', 'PAPA DA VINCI LLC', 'PRIMANTI BROS', 
  'MERO OAKLAND INC', 'CARNEGIE MUSEUM OF ART & NAT HIST', 
  'NEXT CHAPTER WINES & SPIRITS LLC', 'THE CRICKET LOUNGE', 
  'GIANT EAGLE INC', "MITCHELL'S TAVERN & RESTAURANT", 'CARNEGIE MELLON UNIVERSITY', 
  'KHALILS RESTAURANT', "UNCLE JIMMY'S", 'THE GREEK COMMUNITY OF ALLEGHENY COUNTY PA', 
  'CARLOW UNIVERSITY', '5TH YEAR INC', 'MERO CHIKN INC', 'THE OAKLANDER', 
  'EMILIANOS CENTRE AVENUE LLC', 'LUCCA RISTORANTE', 'CARNEGIE MELLON UNIVERSITY', 
  "ZARRA'S"];
  
  $('#the-basics .typeahead').typeahead({
    hint: true,
    highlight: true,
    minLength: 1
  },
  {
    name: 'states',
    source: substringMatcher(states)
  });