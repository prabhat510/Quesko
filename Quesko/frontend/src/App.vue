<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
  </div>
</template>

<script>
import NavbarComponent from "@/components/Navbar.vue";
import { apiService } from "@/common/api.service.js";
export default {
  name: "App",
  components: {
    NavbarComponent,
  },
  methods: {
    async setUserInfo(){
      const data = await apiService("/api/user/")
      const requestUser = data["username"]
      // saving user to local storage so that other components can use to give permissions on likes, delete, edit etc.
      window.localStorage.setItem("username", requestUser)

    }
  },
  created() {
    this.setUserInfo()
  },
};
</script>

<style>
html,body {
  height: 100%;
  font-family: "Playfair Display", serif;
  background-color: #FFFAF0;
}

.btn:focus {
  box-shadow: none;
}
</style>
