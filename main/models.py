from django.db import models



class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True) # não permitir duplicidade

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='projects') # muitos para muitos
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title



# para utilizar multiplas imagens em um project (postagem - produto)

class ProjectImage(models.Model):
    # project pode ter varias images mais cada image só pode ter um project
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE) # exclui todas as images associadas ao projeto excluido
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f'{self.project.title} Image'