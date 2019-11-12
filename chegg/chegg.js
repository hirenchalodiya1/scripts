var waitForEl = function(selector, callback) {
  if (jQuery(selector).length) {
    callback();
  } else {
    setTimeout(function() {
      waitForEl(selector, callback);
    }, 100);
  }
};

function getSols() {
  var x = 1;
  $(".chapters > .chapter").each(function() {
    this.children[0].click();
    $(".problems > .problem").each(function() {
      this.click();

      waitForEl(".problem-content", function() {
        console.log($(".problem-content")[0]);
      });
      waitForEl(".steps", function() {
        console.log($(".solution")[0]);
      });
      if (x == 2) return;
      x++;
    });
    if (x == 2) return;
  });
}

function getSols2() {
  var x = 0;
  $(".chapters > .chapter")[0].children[0].click();
  //   $(".problems > .problem").each(function() {
  //     this.click();
  while (1) {
    $(".problems > .problem")[x].click();
    waitForEl(".problem-content", function() {
      console.log($(".problem-content")[0]);
    });
    waitForEl(".steps", function() {
      console.log($(".solution")[0]);
    });
    if (x == 2) return;
    x++;
  }
  //   });
  if (x == 2) return;
}

function wait(selector) {
  if ($(selector).length === 1) {
    console.log($(selector)[0]);
  } else {
    console.log("Waiting");
    wait(selector);
  }
}
function sleep(delay) {
  var start = new Date().getTime();
  while (new Date().getTime() < start + delay);
}

function sleep2(selector) {
  console.log(typeof $(selector));
}
function sol(x) {
  $(".problems > .problem")[x].click();
}
function so(x) {
  console.log(1);
  setTimeout(sol(x), 300000);
}
function getSols3() {
  $(".chapters > .chapter")[1].children[0].click();
  var x = 0;
  while (x < 3) {
    console.log(13);
    so(x);
    //   setTimeout(sol(x), 300000);
    // sleep2($(".steps"));
    x++;
  }
}

$(".problems > .problem")[1].click();
waitForEl(".problem-content", function() {
  console.log($(".problem-content")[0]);
});
waitForEl(".steps", function() {
  console.log($(".solution")[0]);
});

var chapterIds = [];
$(".chapters > .chapter").each(function() {
  chapterIds.push(this.dataset.id);
});
console.log(chapterIds);

$('[data-id="1409384"]').addClass("open current");

function getSols4() {
  var x = 1;
  $(".chapters > .chapter").each(function() {
    this.children[0].click();
    $(".problems > .problem").each(function() {
      this.click();

      $(document).arrive(".problem-content", function() {
        var $newElem = $(this);
        console.log($newElem[0]);
      });
      $(document).arrive(".steps", function() {
        var $newElem = $(this);
        console.log($newElem[0]);
      });
      x++;
    });
    if (x == 2) return;
  });
}

function getSols5() {
  $(".chapters > .chapter")[1].children[0].click();
  $(".problems > .problem").each(function() {
    this.click();
    console.log(13);
    $(document).arrive(".problem-content", function() {
      var $newElem = $(this);
      console.log($newElem[0]);
    });

    $(document).arrive(".steps", function() {
      var $newElem = $(this);
      console.log($newElem[0]);
    });
  });
}



var waitForEl = function(selector, callback) {
  if (jQuery(selector).length) {
    callback();
  } else {
    setTimeout(function() {
      waitForEl(selector, callback);
    }, 100);
  }
};

function getanswer(){
  waitForEl(".steps", function() {
    console.log($(".solution")[0]);
  });
}

function getSols2() {
  var x = 0;
  $(".chapters > .chapter")[0].children[0].click();
  while (1) {
    $(".problems > .problem")[x].click();
    waitForEl(".problem-content", function() {
      console.log($(".problem-content")[0]);
    });
    for(var i=0;i<10000;){
      i++;
      console.log(x);
    }
    // setTimeout(getanswer,  1000);
    if (x == 2) return;
    x++;
  }
  //   });
  if (x == 2) return;
}
