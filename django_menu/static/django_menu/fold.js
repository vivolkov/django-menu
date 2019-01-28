const togglers = document.querySelectorAll(".toggler");
for(let i = 0; i < togglers.length; i++) {
  togglers[i].addEventListener('click', toggleVisibility);
};

function toggleVisibility() {
    list = this.nextElementSibling;
    desc = list.children;
    for(let i=0; i < list.childElementCount; i++) {
        desc[i].classList.toggle("invisible");
        }
};

let init = document.querySelectorAll(".large > .inner > .large > a.toggler");
console.log(init);
for(let i = 0; i < init.length; i++) {
    console.log(init[i]);
    init[i].click();
}    

