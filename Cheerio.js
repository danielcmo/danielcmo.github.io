const axios = require('axios');
const cheerio = require('cheerio');

async function fetchDBLPData() {
  const url = 'https://dblp.org/pid/68/7553-1.html';
  const { data } = await axios.get(url);
  const $ = cheerio.load(data);

  // Extract publication titles and co-authors
  const publications = [];
  $('div.pub').each((i, el) => {
    const title = $(el).find('span.title').text().trim();
    const authors = $(el).find('span.authors').text().trim().split(',').map(a => a.trim());
    publications.push({ title, authors });
  });

  return publications;
}
