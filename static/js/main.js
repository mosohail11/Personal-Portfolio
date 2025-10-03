document.addEventListener('DOMContentLoaded', () => {
  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  const toggle = document.getElementById('nav-toggle');
  const mobile = document.querySelector('.mobile-nav');
  if (toggle && mobile) {
    toggle.addEventListener('click', () => {
      mobile.classList.toggle('hidden');
    });
  }
});
