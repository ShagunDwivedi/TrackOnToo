<template>
  <div><span v-if="!msg">Deleting.....</span>
    {{ msg }}<br>
    <a @click="pushDash">Back to Dash</a>
  </div>
</template>
<script>
function json(response) {
  return response.json();
}
export default {
  name: 'TrackerDel',
  data() {
    return {
      msg: '',
      trackid: localStorage.getItem('id'),
    };
  },
  mounted() {
    fetch(`http://127.0.0.1:5000/api/tracker/${this.trackid}`, {
      method: 'delete',
      headers: {
        Authorization: localStorage.getItem('access_token'),
      },
    })
      .then(json)
      .then((data) => {
        if (data.msg) {
          this.msg = data.msg;
          this.$router.push('/dashboard');
        }
      });
  },
  methods: {
    pushDash() {
      this.$router.push('/dashboard');
    },
  },
};
</script>

<style scoped>
    body{
background-color: #ffbbb1;
background-attachment: fixed;
background-size: cover;
background-repeat: no-repeat;
background-position: center center;
margin-top: 0px;
margin-left: 0px;
margin-right: 0px;
}
.trkname{
  display: block;
  padding-inline-start: 40px;
  background-color: #653187;
  overflow: hidden;
  margin-top: 0px;
  color: white;
}
a:hover {
  color:#653187;
  cursor: pointer;
}
ul {
  list-style-type: none;
  margin: 5px;
  padding: 8px;
  background-color: #FFDAC1;
  overflow: hidden;
  color: black;
  width: 60%
}

li {
  float: left;
  display: block;
  border-right: 1px solid black;
}

li a{
  display: block;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  cursor: pointer;
}

/* Change the link color to #111 (black) on hover */
li a:hover {
  color: white;
}
.btn{
  width: 10%;
  background-color: #653187;
  cursor: pointer;
  padding: 10px 8px;
  border: none;
  color: white;
  margin-left: 5px;
}
.btn:hover{
  background-color: #FFDAC1;
  color: #653187;
}
fieldset{
  display: block;
  background-color: #ffbbb1;
  width: 50%;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  border-style: none;
}
  </style>
