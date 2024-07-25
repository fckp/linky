$("#create-new-url").on("submit", (event) => {
    event.preventDefault();
    const id = $("#create-new-url > #url-id").val();
    const redir_to = $("#create-new-url > #url-redir").val();
    $.post("/api/url", {
        "id": id,
        "redir_to": redir_to
    }, (data, status) => {
        $(".links").prepend(`<div class="link"><span class="link-id">${data.id}</span><span class="link-url">${data.url}</span><span class="link-actions"><a class="button" href="/${data.id}">Link</a><a class="button delete" href="/api/url/${data.id}">Delete</a></span></div>`);
    })
});

$(".button").on("click", (event) => {
    event.preventDefault();
    
    const url = event.target.href;
    const isDelete = event.target.classList.contains("delete");

    if (isDelete) {
        $.ajax({
            type: "DELETE",
            url: url,
            success: () => {
                const link = event.target.parentNode.parentNode;
                link.parentNode.removeChild(link);
            } 
        });
    }
});