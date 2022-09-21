<template>
  <div>
    {{ this.tracker }}
    <h1 style="margin-left: 5px">Welcome!</h1>
<h3 style="margin-left: 5px">Your Trackers</h3>
<button class="btn" type="submit" @click="addTrk">Add Tracker</button>
<br>
<br>
<ul v-if="this.tracker" style="color:white; background-color: #653187">
<li>  &emsp;Tracker Name  &emsp;</li>
<li>  &emsp;&emsp;Details  &emsp;</li>
<li style="float:right; border-right: none">&emsp;&emsp;Actions&emsp;</li>
</ul>

<span v-for="trkr in this.tracker" :key="trkr">
<br>
<ul>
<li><a href="/:tracker.id">{{ trkr }}&emsp;</a></li>
<li><a href="/:tracker.id">{{ trkr.description }}&emsp;</a></li>
<div style="float:right;">
<li><a href="/:tracker.id/update">Update Tracker</a></li>
<li style="float:right; border-right: none"><a href="/:tracker.trk_id/delete">
  Delete Tracker</a></li>
</div>
</ul>
<br>
</span>
<p v-if="tracker" style="margin-left: 5px">No Trackers Yet.</p>

<br><br><br><br>
</div>
</template>

<script>
function json(response) {
  return response.json();
}
export default {
  name: 'Dashboard',
  tracker: '',
  mounted() {
    fetch('http://127.0.0.1:5000/api/trackers', {
      method: 'get',
      headers: {
        Authorization: localStorage.getItem('access_token'),
      },
    })
      .then(json)
      .then((data) => {
        if (data.msg) {
          this.tracker = '';
        } else {
          localStorage.setItem('tracker', JSON.stringify(data));
          this.tracker = JSON.parse(localStorage.getItem('tracker'));
        }
      });
  },
  methods: {
    addTrk() {
      this.$router.push('/addtracker');
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
ul {
  list-style-type: none;
  margin: 5px;
  padding: 8px;
  background-color: #FFDAC1;
  overflow: hidden;
  color: black;
  width: 70%;
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
