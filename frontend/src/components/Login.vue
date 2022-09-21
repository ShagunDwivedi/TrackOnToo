<template>
  <div>
    <!--Heheheh-->
    <!--input v-model="text"-->
<fieldset>
<h4>Login</h4>
<span v-if="msg">{{ msg }} <br></span>
<!--{{ msg }}<br>-->
<label for="email">Username</label><br>
<input id="email" name="email" required v-model="username">
<br><br>
<label for="password">Password</label><br>
<input id="password" name="password" required type="password" v-model="password">
<br><br>
<button id="submit" name="submit" type="submit" class="btn" @click.prevent="submitted">Login
</button>
<br><br>
</fieldset>
</div>
</template>

<script>
import { mapMutations } from 'vuex';

function json(response) {
  return response.json();
}
export default {
  name: 'Login',
  data() {
    return {
      msg: '',
      username: '',
      password: '',
    };
  },
  methods: {
    ...mapMutations(['setUser', 'setToken']),
    submitted() {
      fetch('http://127.0.0.1:5000/api/login', {
        method: 'post',
        headers: {
          'Content-type': 'application/json',
        },
        body: JSON.stringify({ username: this.username, password: this.password }),
      })
        .then(json)
        .then((data) => {
          if (data.access_token) {
            localStorage.setItem('username', data.username);
            localStorage.setItem('access_token', `Bearer ${data.access_token}`);
            this.$router.push('/dashboard');
          } else {
            this.msg = data.msg;
          }
        });
    },
  },
};

</script>

<style scoped>
fieldset{
  display: block;
  background-color:#653187;
  width: 50%;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  color: white;
  border-style: none;
}

.btn{
  width: 20%;
  background-color: white;
  color: #653187;
  cursor: pointer;
  padding: 10px 16px;
  border: none;
}
.btn:hover{
  background-color: #ffbbb1;
  color: white;
}
.trkname{
  display: block;
  padding-inline-start: 40px;
  background-color: #653187;
  overflow: hidden;
  margin-top: 0px;
  color: white;
}
a:link {
color: white;
}
a:visited {
color: white;
}
a:hover {
color: #ffbbb1;
}
a:active {
color: white;
}
</style>
