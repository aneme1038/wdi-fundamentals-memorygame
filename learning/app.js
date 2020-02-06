$(() => {
  const $btn = $('#btn1');
  $($btn).on('click', (event) => {
    console.log("this is working");
    $.ajax({
      url: "https://api.pushshift.io/reddit/search/comment/?q=science&subreddit=askscience",
      type: "GET"
    }).then((data) => {
      console.log(data.results);
      const results = data.results;
    })
  })
})
