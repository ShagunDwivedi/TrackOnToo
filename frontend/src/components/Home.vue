<template>
<div class="fieldset">
<br><h3>Track your Activities!</h3>
<h4>New Here? Create an Account!</h4>
<button class="btn" type="submit" @click="pushReg">Sign Up</button>
<br>
<h4>Already Using?</h4>
<button class="btn" type="submit" @click="pushLog">LogIn</button>
<br><br><br>
</div>

</template>

<script>
export default {
  name: 'Home',
  methods: {
    pushReg() {
      this.$router.push('/register');
    },
    pushLog() {
      this.$router.push('/login');
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.fieldset{
  display: block;
  background-color:#653187;
  width: 52%;
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
</style>
