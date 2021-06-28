<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-primary my-navbar">
    <div class="container">
      <router-link :to="{ name: 'home' }" class="navbar-brand"
        >Quesko</router-link
      >
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <!-- name: are used to get proper links and they are defined inside index.js -->
            <router-link :to="{ name: 'home' }" class="btn btn-success"
              >Home</router-link
            >
          </li>
          <li class="nav-item mx-1">
            <router-link
              :to="{ name: 'question-editor' }"
              class="btn btn-danger"
              >Ask Question</router-link
            >
          </li>
          <li class="nav-item ml-1">
            <a class="btn btn-warning" href="/accounts/logout/">Logout</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent",
};
</script>

<style>
.my-navbar {
  border-bottom: 1px solid #ddd;
}
.navbar-brand {
  font-weight: bold;
  font-size: 130%;
}
.navbar-brand:hover {
  color: red !important;
}
.container {
  font-weight: bold;
}
</style>