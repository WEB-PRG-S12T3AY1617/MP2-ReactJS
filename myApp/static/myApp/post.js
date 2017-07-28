window.onload = function(){
    document.getElementById('posts_15').style.display = 'none';
    document.getElementById('posts_20').style.display = 'none';
    document.getElementById('morePosts_15').style.display = 'none';
    document.getElementById('morePosts_20').style.display = 'none'; document.getElementById('morePosts_10').style.display = 'none';
}
 
function view(){
    var view_by = document.getElementById('dropdown').value;
    console.log(view_by);
   
    if (view_by == '10') {
        document.getElementById('morePosts_15').style.display = 'none';
        document.getElementById('morePosts_20').style.display = 'none'; document.getElementById('morePosts_10').style.display = 'none';
        document.getElementById("posts_10").style.display = 'block';
        document.getElementById("posts_15").style.display = 'none';
        document.getElementById("posts_20").style.display = 'none';
        
    }
    else if (view_by == '15') {
        document.getElementById('morePosts_15').style.display = 'none';
        document.getElementById('morePosts_20').style.display = 'none'; document.getElementById('morePosts_10').style.display = 'none';
        document.getElementById("morebtn").style.display= 'none';
        document.getElementById("posts_10").style.display = 'none';
        document.getElementById("posts_20").style.display = 'none';
        document.getElementById("posts_15").style.display = 'block';
    }
    else if (view_by == '20') {
        document.getElementById('morePosts_15').style.display = 'none';
        document.getElementById('morePosts_20').style.display = 'none'; document.getElementById('morePosts_10').style.display = 'none';
        document.getElementById("morebtn").style.display= 'none';
        document.getElementById("posts_10").style.display = 'none';
        document.getElementById("posts_15").style.display = 'none';
        document.getElementById("posts_20").style.display = 'block';
    }
    
      document.getElementById("morebtn").style.display= 'block';
}

function viewMore() {
    var view_by = document.getElementById('dropdown').value;
    
    if (view_by == '10') {
        document.getElementById("morebtn").style.display= 'none';
        document.getElementById("posts_10").style.display= 'none';
        document.getElementById("morePosts_10").style.display = 'block';
        document.getElementById("morePosts_15").style.display = 'none';
        document.getElementById("morePosts_20").style.display = 'none';
    }
    else if (view_by == '15') {
        document.getElementById("morebtn").style.display= 'none';
        document.getElementById("posts_15").style.display= 'none';
        document.getElementById("morePosts_15").style.display = 'block';
        document.getElementById("morePosts_20").style.display = 'none';
        document.getElementById("morePosts_10").style.display = 'none';
    }
    else if (view_by == '20') {
        document.getElementById("morebtn").style.display= 'none';
        document.getElementById("posts_20").style.display= 'none';
        document.getElementById("morePosts_10").style.display = 'none';
        document.getElementById("morePosts_15").style.display = 'none';
        document.getElementById("morePosts_20").style.display = 'block';
    }
    
}