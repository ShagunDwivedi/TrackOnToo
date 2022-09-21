<template>
  <div>
    <fieldset>
      <h4>Enter Details</h4>
      <span v-if="msg">{{ msg }} <br><br></span>
      <label for="id">Pick a Username</label><br>
        <input id="id" name="id" required type="text" v-model="username"><br><br>
        <label for="name">Enter Your Name</label><br>
        <input id="name" name="name" required type="text" v-model="name"><br><br>
        <label for="email">Email Address</label><br>
        <input id="email" name="email" required type="text" v-model="email"><br><br>
        <label for="password">Password</label> <br>
        <input id="password" name="password" type="password" v-model="password"><br>
        <br><br>
        <button id="submit" name="submit" type="submit" class="btn" @click.prevent="submitted">
          SignUp
        </button>
        <br><br>
        <!---<input class="btn" id="submit" name="submit" type="submit" value="Register"><br><br>-->
      </fieldset>
  </div>
</template>

<script>
function json(response) {
  return response.json();
}
export default {
  name: 'Register',
  data() {
    return {
      msg: '',
      username: '',
      email: '',
      password: '',
      name: '',
    };
  },
  methods: {
    login() {
      fetch('http://127.0.0.1:5000/api/login', {
        method: 'post',
        headers: {
          'Content-type': 'application/json',
        },
        body: JSON.stringify({ username: this.username, password: this.password }),
      })
        .then(json)
        .then((data) => {
          localStorage.setItem('username', data.username);
          localStorage.setItem('access_token', `Bearer ${data.access_token}`);
          this.$router.push('/dashboard');
        });
    },
    submitted() {
      fetch('http://127.0.0.1:5000/api/signup', {
        method: 'post',
        headers: {
          'Content-type': 'application/json',
        },
        body: JSON.stringify({
          username: this.username, password: this.password, name: this.name, email: this.email,
        }),
      })
        .then(json)
        .then((data) => {
          if (data.msg === 'Created') {
            this.login();
          } else this.msg = data.msg;
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
  color:#653187;
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
