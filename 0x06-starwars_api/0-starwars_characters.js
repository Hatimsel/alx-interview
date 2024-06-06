#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
	console.error('Error fetching film data:', error);
	return;
  }

  const characterUrls = JSON.parse(body).characters;
  fetchCharacterNamesInOrder(characterUrls, 0);
});

const fetchCharacterNamesInOrder = (urls, index) => {
  if (index === urls.length) return;

  request(urls[index], function (error, response, body) {
	if (error) {
	console.error('Error fetching character data:', error);
	return;
	}

	console.log(JSON.parse(body).name);
	fetchCharacterNamesInOrder(urls, index + 1);
  });
};
