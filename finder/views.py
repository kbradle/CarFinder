import os

from ml import predictor
from django.shortcuts import render
from django.views import View
from django.core.files.storage import FileSystemStorage

class Index(View):
    submitted = False
    def __init__(self):
        self._template = 'index.html'
        self._checkpoint_path = 'ml/model/checkpoint.pth'

        self._predictor = predictor.Predictor(self._checkpoint_path)
        self._classes = self._predictor.classes

    def get(self, request):
        return render(request, self._template)

    def predict_image(self, request):
        image_obj = request.FILES.get('filePath', None)

        # if user did not upload an image, refresh
        if image_obj is None:
            return render(request, 'upload.html')

        fs = FileSystemStorage()

        # save the file and get the path
        image_name = fs.get_available_name(image_obj.name)
        image_path = fs.save(image_name, image_obj)
        image_path = fs.url(image_path)
        full_image_path = os.path.join('lib','python3.8','site-packages','finder', 'static', 'media', image_name)

        # get prediction
        try:
            pred_confs, pred_classes = self._predictor.predict(full_image_path)
        except:
            context = {
                'errorMessage': 'There was an error processing your image. Make sure it is not a corrupted image file.'
            }
            return render(request, 'error.html', context)
        
        predicted_class = self._classes[pred_classes[0]]
        
        # plot confidence scores
        plot_image_name = fs.get_available_name('plot.png')
        plot_image_path = os.path.join('media', plot_image_name)
        full_plot_image_path = os.path.join('lib','python3.8','site-packages','finder', 'static', plot_image_path)
        self._predictor.plot_predictions(pred_confs, pred_classes, full_plot_image_path)

        submitted = True

        # update upload.html with context
        context={
            'predictedLabel': predicted_class,
            'imagePath': image_path,
            'plotImagePath': f'/{plot_image_path}',
            'submitted': submitted
        }
        return render(request,'upload.html',context)

    def list_of_cars(self,request):
        return render(request, 'listOfCars.html')

def error_404(request, exception):
    return render(request, 'index.html', status=404)