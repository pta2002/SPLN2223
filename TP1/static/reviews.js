document.querySelectorAll('.scores').forEach(el => {
  el.querySelector('a').addEventListener('click', e => {
    el.innerHTML = "Calculating...";
    fetch(`/reviews/${el.getAttribute('review-id')}/polarity`).then(async res => {
      let json = await res.json();
      el.innerHTML = json["compound"] > 0 ? "👍" : "👎";
    })
    e.preventDefault()
  })
})
