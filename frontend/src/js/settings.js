const themeToggle = document.getElementById("theme-toggle")
themeToggle.addEventListener("change", () => {
  document.documentElement.classList.toggle("dark")
  localStorage.setItem("theme", themeToggle.checked ? "dark" : "light")
})
if (localStorage.getItem("theme") === "dark") {
  themeToggle.checked = true
  document.documentElement.classList.add("dark")
}

// Notify toggles are in localStorage too, but skipped for brevity
