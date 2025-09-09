const Index = () => {
  return (
    <div className="min-h-screen flex items-center justify-center relative overflow-hidden">
      {/* Background gradient circles for depth */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-primary/10 rounded-full blur-3xl animate-pulse"></div>
      <div className="absolute bottom-1/4 right-1/4 w-80 h-80 bg-primary/5 rounded-full blur-3xl animate-pulse delay-1000"></div>
      
      {/* Main content */}
      <div className="text-center space-y-8 animate-fade-in">
        <div className="space-y-4">
          <h1 className="text-8xl md:text-9xl font-bold tracking-tight animate-slide-up">
            <span className="text-gradient">Hello</span>
          </h1>
          <p className="text-xl md:text-2xl text-muted-foreground max-w-md mx-auto animate-slide-up delay-300">
            Welcome to something beautiful
          </p>
        </div>
        
        {/* Subtle glow effect */}
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-2 h-2 bg-primary rounded-full shadow-glow animate-pulse -z-10"></div>
      </div>
    </div>
  );
};

export default Index;