window.onload = function(){
    document.getElementById('all_posts').style.display = 'none';
}


function viewPosts()
{
    var x = document.getElementById('posts');
    x.style.display = 'none';
    var button = document.getElementById('morebtn');
    button.style.display = 'none';
    
    var y = document.getElementById('all_posts');
    y.style.display = 'block';
}