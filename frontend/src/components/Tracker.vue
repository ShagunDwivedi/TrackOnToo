<template>
  <div>
    <a href="/dashboard" style="margin-left: 5px">Back to Dashboard</a>
<h1 style="margin-left: 5px">{{ tracker.trk_name }}</h1>
<h5 style="margin-left: 5px">Tracker Description: {{ tracker.description }}</h5>
{% if loglist|length !=0 %}
<!-- eslint-disable-next-line max-len -->
<!-- img src="{{url_for('static', filename='plot.jpg')}}" style="margin-left: 15px" height=35% width=40% --><br>
{% endif %}
<form action="/:tracker.trk_id/addlog" method="get">
<input class="btn" type="submit" value="Add New Log">
</form>
<br>
{% if loglist|length !=0 %}
<ul style="color:white; background-color: #ffbbb1">
<li>  &emsp;Last Updated  &emsp;</li>
<li>  &emsp;Value  &emsp;</li>
<li>  &emsp;&emsp;Details  &emsp;</li>
<li style="float:right; border-right: none">&emsp;&emsp;Actions&emsp;</li>
</ul>
<br>
{% for logged in loglist %}
<ul>
<li>{{ logged.time }}&emsp;</li>
<li>&emsp;{{ logged.value }}&emsp;</li>
<li>&emsp;{{ logged.note }}&emsp;</li>
<div style="float:right;">
<li><a href="/:tracker.trk_id/:logged.log_id/updatelog">Update&emsp;</a></li>
<!-- eslint-disable-next-line max-len -->
<li style="float:right; border-right: none"><a href="/:tracker.trk_id/:logged.log_id/deletelog">&emsp;Delete</a></li>
</div>
</ul>
<br>
{% endfor %}
{% else %}
<p style="margin-left: 5px">No Logs Yet.</p>
{% endif %}
</div>
</template>

<script>
export default {
  name: 'Tracker',
};
</script>

<style>
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
  background-color: #ffbbb1;
  color: #653187;
}
</style>
