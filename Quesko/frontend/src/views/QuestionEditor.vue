<template>
  <div class="container mt-2">
    <h1 class="mb-3">Ask a Question:</h1>
    <form @submit.prevent="onSubmit">
      <textarea
        rows="8"
        v-model="question_body"
        class="form-control font"
        placeholder="What do you want to ask?"
      ></textarea>
      <br />
      <button type="submit" class="btn btn-success">Publish</button>
    </form>
    <div v-if="error" class="muted mystyle mt-2">{{ error }}</div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "QuestionEditor",
  data() {
    return {
      question_body: null,
      error: null,
    };
  },
  props: {
    slug: {
      type: String,
      required: false,
    },
  },
  methods: {
    onSubmit() {
      if (!this.question_body) {
        this.error = "You can't send an empty question";
      } else if (this.question_body.length > 240) {
        this.error = "questions must not be longer than 240 characters";
      } else {
        let endpoint = `/api/questions/`;
        let method = "POST";
        if (this.slug !== undefined) {
          endpoint += `${this.slug}/`;
          method = "PUT";
        }
        apiService(endpoint, method, { content: this.question_body }).then(
          (data) => {
            this.$router.push({
              name: "question",
              params: { slug: data.slug },
            });
          }
        );
      }
    },
    async beforeRouteEnter(to, from, next) {
      if (to.params !== undefined) {
        let endpoint = `/api/questions/${to.params.slug}/`;
        let data = await apiService(endpoint);
        return next((vm) => (vm.question_body = data.content));
      } else {
        return next();
      }
    },
  },

  created() {
    document.title = "Editor - QuestionTime";
  },
};
</script>

<style>
.font {
  font-family: "Noto Serif", serif;
}
.mystyle {
  font-family: Verdana, Geneva, Tahoma, sans-serif;
  font-size: 20px;
  color: red;
}
</style>
