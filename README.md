# FLASK-HTMX

Vous avez appris FLASK et javascript vous donne envie de voumir alors <a href="https://htmx.org/">HTMX</a> est fait pour vous.
> Je veux être clair: on ne peut pas faire du web sans javascript. HTMX c'est faire du javascript (AJAX) dans écrire du javascript.

Le HTML devient magique, un simple attribut ajouté à tag html, une requête est lancée. 

~~~html
<form 
    hx-post="{{ url_for('add_person') }}" 
    hx-target="#persons-list" 
    hx-swap="beforeend"
    hx-on="htmx:afterRequest: this.remove()"
    hx-trigger="click from:#submit-all"
    class="my-3"
>
    <div class="row">
        <div class="col-md-5">
            <div class="mb-3">
                <label for="fist_name">{{ form.first_name.label(class_="form-label") }}:</label>
                {{ form.first_name(class_="form-control") }}
            </div>
        </div>
        <div class="col-md-5">
            <div class="mb-3">
                <label for="last_name">{{ form.last_name.label(class_="form-label") }}:</label>
                {{ form.last_name(class_="form-control") }}
            </div>
        </div>
        <div class="col-md-2 align-self-end mb-3">
            <button 
                type="button" 
                class="btn btn-danger"
                hx-on="click: this.closest('form').remove()"
            >
                Annuler
            </button>
        </div>
    </div>
</form>
~~~

## Explications:


- <code>hx-post="{{ url_for('add_person') }}"</code>: cette ligne signifie: lance une requête post à l'url add_person

- <code>hx-target="#persons-list"</code>: Met la réponse renvoyée par hx-post dans la div ayant id persons-list

- <code>hx-swap="beforeend"</code>: Ne met pas la réponse obtenue n'importe où mais avant la fin de la div ayant l'id persons-list

- <code>hx-on="htmx:afterRequest: this.remove()"</code>: Supprime le formulaire après sumission

- <code>hx-trigger="click from:#submit-all"</code>: Quand on clique sur le bouton ayant l'id submit-all : soumet tous les formulaires

- <code>hx-on="click: this.closest('form').remove()"</code>: Ecoute l'évenement click et supprime l'élement form



