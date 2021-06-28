<template>
  <div class="container mt-2">
    <h1 class="mb-3">Edit Your Answer:</h1>
    <form @submit.prevent="onSubmit">
      <textarea rows="8" v-model="answerBody" class="form-control font"></textarea>
      <br />
      <button type="submit" class="btn btn-success">Publish Your Answer</button>
    </form>
    <div v-if="error" class="muted mystyle mt-2">{{ error }}</div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "AnswerEditor",
  data() {
    return {
      answerBody: this.previousAnswer,
      error: null
    };
  },
  props: {
    id: {
      type: Number,
      required: true
    },
    previousAnswer: {
      type: String,
      required: true
    },
    questionSlug: {
      type: String,
      required: true
    }
  },
  methods: {
    onSubmit() {
      if (this.answerBody) {
        let endpoint = `/api/answers/${this.id}/`;
        apiService(endpoint, "PUT", { body: this.answerBody }).then(() => {
          this.$router.push({
            name: "question",
            params: { slug: this.questionSlug }
          });
        });
      } else {
        this.error = "You cannot submit an empty answer";
      }
    }
  },
  // this function is executed before entering the route
  // watch video --25
  async beforeRouteEnter(to, from, next) {
    let endpoint = `/api/answers/${to.params.id}/`;
    let data = await apiService(endpoint);
    to.params.previousAnswer = data.body;
    to.params.questionSlug = data.question_slug;
    return next();
  }
};
</script>